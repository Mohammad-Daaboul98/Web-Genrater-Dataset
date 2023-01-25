Generate HTML:
for /r %x in (*.gui) do python ../../../web-compiler.py %x

for %x in (*.gui) do python ../../compiler/web-compiler.py %x


Move & Delete Files:
for /r . %x in (*.html) do move "%x" ../html

for /r . %x in (*.html) do del "%x"







Dataset:
https://drive.google.com/open?id=10y5reqWpbPMC96vE2jky-ujzn196JShl&authuser=junior.colap.22%40gmail.com&usp=drive_fs


API:
https://drive.google.com/open?id=1-AuMksk3cdewluEA9sU6g604hZs2HP11&authuser=junior.colap.22%40gmail.com&usp=drive_fs


Resources:
https://github.com/VaibhavYadav/pytorch_pix2code
https://github.com/tonybeltramelli/pix2code