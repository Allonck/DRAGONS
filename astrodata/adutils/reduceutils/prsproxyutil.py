
from astrodata import AstroData
from astrodata.usercalibrationservice import user_cal_service

from xml.dom import minidom
import exceptions

CALMGR = "http://fits/calmgr"
#CALMGR = "http://hbffits3.hi.gemini.edu/calmgr"
LOCALCALMGR = "http://localhost:%(httpport)d/calsearch.xml?caltype=%(caltype)s"

#LOCALCALMGR = "http://localhost:%(httpport)d/calsearch.xml?caltype=%(caltype)s&%(tokenstr)s"
#"None # needs to have adcc http port in
CALTYPEDICT = { "bias": "bias",
                "dark": "dark",
                "flat": "flat",
                "processed_bias":   "processed_bias",
                "processed_dark":   "processed_dark",
                "processed_flat":   "processed_flat",
                "processed_fringe": "processed_fringe"}

def urljoin(*args):
    for arg in args:
        if arg[-1] == '/':
            arg = arg[-1]
    ret = "/".join(args)
    print "prs31:", repr(args), ret
    return ret

def upload_calibration(filename):
    import urllib, urllib2
    import httplib, mimetypes
    import os

    import sys
    import urllib, urllib2

    fpath = filename
    fn = os.path.basename(fpath)
    fd = open(fpath)
    d = fd.read()
    fd.close()
    
    #url = "http://hbffits3.hi.gemini.edu/upload_processed_cal/"+fn
    url = "http://fits/upload_processed_cal/"+fn

    postdata = d # urllib.urlencode(d)

    try:
        rq = urllib2.Request(url)
        u = urllib2.urlopen(rq, postdata)
        #fp = open("/tmp/tmpfile.txt")
        #raise urllib2.HTTPError("","","","",fp)
        
    except urllib2.HTTPError, error:
        contents = error.read()
        #print "ERROR:"
        #print contents
        raise

    response = u.read()
    #print "RESPONSE"
    #print response


def calibration_search(rq, fullResult = False):
    import urllib, urllib2
    print "ppu68: calibration_search\n" * 6
    from astrodata.FitsStorageFeatures import FitsStorageSetup
    from xmlrpclib import DateTime 
    fss = FitsStorageSetup() # note: uses current working directory!!!
    
    #if "ut_datetime" in rq:
    #    rq["ut_datetime"] = str(rq["ut_datetime"])
    #if not fss.is_setup():
    #    return None
    # print "ppu77:" + repr(rq)
    if "source" not in rq:
        source = "central"
    else:
        source = rq["source"]
    
    token = "" # used for GETs, we're using the post method
    rqurl = None
    if source == "central" or source == "all":
        # print "ppu107: CENTRAL", token
        # print "ppu108: ", rq['caltype']
        
        rqurl = urljoin(CALMGR, CALTYPEDICT[rq['caltype']])
        print "ppu109: CENTRAL SEARCH: rqurl is "+ rqurl
        
    print "ppu112:", source
    if source == 'local' or (rqurl == None and source=="all"):
        rqurl = LOCALCALMGR % { "httpport": 8777,
                                "caltype":CALTYPEDICT[rq['caltype']],
                                } # "tokenstr":tokenstr}
        print "ppu118: LOCAL SEARCH: rqurl is "+ rqurl

    if "?" in rqurl:
        rqurl = rqurl+"&filename=%s"%rq["filename"]
    else:
        rqurl = rqurl+"/filename=%s"%rq["filename"]
    print "prs100:", rqurl
    ### send request
    sequence = [("descriptors", rq["descriptors"]), ("types", rq["types"])]
    postdata = urllib.urlencode(sequence)
    try:
        # print "ppu96: postdata",repr(postdata)
        calRQ = urllib2.Request(rqurl)
        u = urllib2.urlopen(calRQ) #, postdata)
        response = u.read()
    except urllib2.HTTPError, error:
        print "ppu110:HTTPError", error.read()
        import traceback
        traceback.print_exc()
    #response = urllib.urlopen(rqurl).read()
    print "prs129:", response
    if fullResult:
        return response
    dom = minidom.parseString(response)
    calel = dom.getElementsByTagName("calibration")
    try:
        calurlel = dom.getElementsByTagName('url')[0].childNodes[0]
        calurlmd5 = dom.getElementsByTagName('md5')[0].childNodes[0]
    except exceptions.IndexError:
        print "No url for calibration in response, calibration not found"
        return (None,None)
    #print "prs70:", calurlel.data
    
    #@@TODO: test only 
    print "prspu124:", repr(calurlel.data)
    return (calurlel.data, calurlmd5.data)


def old_calibration_search(rq, fullResult = False):
    from astrodata.FitsStorageFeatures import FitsStorageSetup
    fss = FitsStorageSetup() # note: uses current working directory!!!
    print "ppu24: in here"
    if not fss.is_setup():
        return None
    print "prs38: the request",repr(rq)
    if 'caltype' not in rq:
        rq.update({"caltype":"processed_bias"})
    if 'datalabel' not in rq and "filename" not in rq:
        return None
        
    if "filename" in rq:
        import os
        token = os.path.basename(rq["filename"])
        tokenstr = "filename=%s" % token
    elif 'datalabel' in rq:
        token = rq["datalabel"]
        tokenstr = "datalabel=%s" % token
    
    if "source" not in rq:
        source = "central"
    else:
        source = rq["source"]
    
    print "ppu32:", repr(rq), source
    
    rqurl = None
    if source == "central" or source == "all":
        print "ppu52: CENTRAL SEARCH"
        rqurl = urljoin(CALMGR, CALTYPEDICT[rq['caltype']],token)
        print "ppu54: CENTRAL SEARCH: rqurl is "+ rqurl
        
    print "ppu52:", source
    if source == 'local' or (rqurl == None and source=="all"):
        return None
        rqurl = LOCALCALMGR % { "httpport": 8777,
                                "caltype":CALTYPEDICT[rq['caltype']],
                                "tokenstr":tokenstr}
        print "ppu57: LOCAL SEARCH: rqurl is "+ rqurl

    sequence = [("descriptors",rq.descriptors),('types',rq.types)]
    postdata = urllib.urlencode(sequence)
    
    # response = urllib.urlopen(rqurl).read()
    
    webrq = urllib2.Request(rqurl)
    u = urllib2.urlopen(webrq,postdata)
    
    # note: todo: read the request in case of error by except HTTPError
    response = u.read()
    
    
    if fullResult:
        return response
    dom = minidom.parseString(response)
    calel = dom.getElementsByTagName("calibration")
    try:
        calurlel = dom.getElementsByTagName('url')[0].childNodes[0]
    except exceptions.IndexError:
        return None
    #print "prs70:", calurlel.data
    
    #@@TODO: test only 
    return calurlel.data
