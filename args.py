import argparse

parser = argparse.ArgumentParser(description='Calculadora, suma/resta/multiplica a y b')
parser.add_argument('-i', '--image_path', type=str, help='carpeta de imagenes')
#parser.add_argument('-b', '--numero_b', type=int, help='Parámetro b')
parser.add_argument('-o', '--operacion',
                    type=str,
                    choices=['rescale', 'resta', 'multiplicacion'],
                    default='suma', required=False,
                    help='Operación a realizar con a y b')

args = parser.parse_args()

if args.operacion == 'suma':
    print(args.numero_a + args.numero_b)
elif args.operacion == 'resta':
    print(args.numero_a - args.numero_b)
elif args.operacion == 'multiplicacion':
    print(args.numero_a * args.numero_b)