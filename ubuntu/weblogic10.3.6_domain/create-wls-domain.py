# Default domain 'base_domain' to be created inside the Docker image for WLS
# ==============================================

# Open default domain template
# ======================
readTemplate("/root/Oracle/Middleware/wlserver_10.3/common/templates/domains/wls.jar")

# Configure the Administration Server and SSL port.
# =========================================================
cd('Servers/AdminServer')
set('ListenAddress','')
set('ListenPort', 7001)

# Define the user password for weblogic
# =====================================
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('Oracle@123')

# Write the domain and close the domain template
# ==============================================
setOption('OverwriteDomain', 'true')

writeDomain('/root/Oracle/Middleware/user_projects/domains/base_domain')
closeTemplate()

# Exit WLST
# =========
exit()