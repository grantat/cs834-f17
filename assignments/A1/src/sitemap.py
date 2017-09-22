import os
from datetime import datetime
import xml.etree.ElementTree as ET


def indent(elem, level=0, more_sibs=False):
    '''
    Pretty print xml etree
    '''
    i = "\n"
    if level:
        i += (level - 1) * '  '
    num_kids = len(elem)
    if num_kids:
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
            if level:
                elem.text += '  '
        count = 0
        for kid in elem:
            indent(kid, level + 1, count < num_kids - 1)
            count += 1
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
            if more_sibs:
                elem.tail += '  '
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
            if more_sibs:
                elem.tail += '  '


def getLastModified(filePath):
    '''
    Get last modified datetime of a file
    '''
    stat = os.stat(filePath)
    dtime = datetime.fromtimestamp(
        stat.st_mtime).strftime("%Y-%m-%dT%H:%M:%SZ")
    return dtime


def buildSitemap(outfile, baseURL, rootdir):
    '''
    build xml tree for directory based sitemap
    '''
    urlset = ET.Element(
        'urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    with open(outfile, 'w'):
        for subdir, dirs, files in os.walk(rootdir):
            for f in files:
                filepath = subdir + os.sep + f
                lastmod = getLastModified(filepath)
                url = ET.Element('url')
                # remove './' from path as start of a string
                if filepath.startswith(rootdir + os.sep):
                    filepath = filepath[len(rootdir + os.sep):]
                elif filepath.startswith(rootdir):
                    filepath = filepath[len(rootdir):]

                filepath = filepath.replace(' ', '+')
                loc = ET.SubElement(url, 'loc')
                loc.text = baseURL + filepath
                lastmods = ET.SubElement(url, 'lastmod')
                lastmods.text = lastmod
                urlset.append(url)

        indent(urlset)
        tree = ET.ElementTree(urlset)
        tree.write(outfile, encoding='utf-8', xml_declaration=True)


if __name__ == "__main__":
    baseURL = "http://example.com/"

    if baseURL.endswith('/') is False:
        baseURL += '/'

    outfile = 'data/sitemap.xml'
    buildSitemap(outfile, baseURL, '../..')
