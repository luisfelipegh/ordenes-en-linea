from Usuario import Usuario
from Perfil import Perfil
from Orden import Orden


if __name__ == '__main__':
    perfilAdmin = Perfil('admin')
    perfilUser = Perfil('user')
    perfilBiller = Perfil('biller')

    pepe = Usuario('pepe', 'pepe123', perfilUser)
    pepeAdmin = Usuario('pepeAdmin', 'pepe123', perfilAdmin)
    pepeBiller = Usuario('pepeBiller', 'pepe123', perfilBiller)

    ordenPepe = Orden()
    ordenPepeAdmin = Orden()
    ordenPepeBiller = Orden()

    ordenPepe = ordenPepe.validarOrden(pepe)
    ordenPepeAdmin = ordenPepeAdmin.validarOrden(pepeAdmin)
    ordenPepeBiller = ordenPepeBiller.validarOrden(pepeBiller)

    print('Orden de pepe con estado: ', ordenPepe.estado, '  paso por los validadores: ' , ordenPepe.validadores)

    print('Orden de pepe Admin con estado: ', ordenPepeAdmin.estado, '  paso por los validadores: ' , ordenPepeAdmin.validadores)

    print('Orden de pepe Biller con estado: ', ordenPepeBiller.estado, '  paso por los validadores: ' , ordenPepeBiller.validadores)

