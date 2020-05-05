# Test case for dh-virtualenv #299

## build

     dpkg-buildpackage -uc -us

results in 

    dh_install: Cannot find (any matches for) "etc/uwsgi.ini" (tried in debian/dhv-299-0.0.1, debian/tmp)

