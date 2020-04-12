from utilities.InicioSesion import SingUp
from utilities.INFO_SEARCH_TEST import Logs
from utilities.ADMIN_MODULE_TEST import LogAdmin
import codecs
import sys
su = SingUp()
driver = su.startLogin(use=True)
if driver is not None:
    driver.close()


try:
    buildjson = "{\n\"modulo\"       : \"" +"Solcitudes"+"\"," \
                 "\n\"filtro\"       : \"" +"fecha"+"\"," \
                 "\n\"buscarPor\"    : \"" +"Responsable"+"\"," \
                 "\n\"busca\"        : \"" +""+"\","\
                 "\n\"fechaInicio\"  : \"" +"30/05/2014"+"\"," \
                 "\n\"fechaFinal\"   : \"" +"23/06/2019"+"\"\n}"

    f = codecs.open("../utilities/data2.txt", 'w', "utf-8")
    f.write(str(buildjson)+"\n#-comments-#")
    f.close()
    l = Logs()
    l.startTest(use=False)
except:
    print("Busqueda finalizada, no se encontraron datos con esos parametros.",sys.exc_info())

