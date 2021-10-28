
#!/usr/bin/env python

import sys
import site

site.addsitedir('/usr/share/httpd/noindex')

sys.path.insert(0, '/usr/share/httpd/noindex')

from app import app as application
#import app as application
