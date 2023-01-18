Generate HTML:
for /r %x in (*.gui) do python ../../../web-compiler.py %x

for %x in (*.gui) do python ../../compiler/web-compiler.py %x


Move & Delete Files:
for /r . %x in (*.html) do move "%x" ../html

for /r . %x in (*.html) do del "%x"








Resource:
https://github.com/VaibhavYadav/pytorch_pix2code