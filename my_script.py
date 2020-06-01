from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is my message')
encoder.save('./datamatrix.png')
print(encoder.get_ascii())
