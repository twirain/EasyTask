import argparse
import os

import env
import output

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--jks', required=False, help='java key store file')
    parser.add_argument('--apk', required=False, help='apk file to print cert info')
    parser.add_argument('--storepass', required=False, help='jks storepass')
    args = parser.parse_args()

    if not env.has_executable('keytool'):
        output.print_red('未找到keytool程序，请检查是否有Java环境')
        exit(-1)

    if args.jks is not None:
        os.system(f"keytool -v -list -keystore {args.jks} -storepass {args.storepass}")
    elif args.apk is not None:
        os.system(f"keytool -printcert -jarfile {args.apk}")
