Generate HTML:
for /r %x in (*.gui) do python ../../../web-compiler.py %x

Move HTML:
for /r . %x in (*.html) do move "%x" ../html

Move PNG:
for /r . %x in (*.png) do move "%x" ../png


Try without /r




Resource:
https://github.com/VaibhavYadav/pytorch_pix2code