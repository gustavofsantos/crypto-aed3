echo -n $1 | openssl dgst -md5 | sed 's/^.* //' | openssl base64

# Hash original:             AKCkKOEHZuUPfCLbS0ye8WFnXoDEgw9RFYXlw293vbY=
#                            MjVkNTVhZDI4M2FhNDAwYWY0NjRjNzZkNzEzYzA3YWQK
#                            MWNhMzA4ZGY2Y2RiMGE4YmY0MGQ1OWJlMmExN2VhYzEgYmFzZTY0Cg==
#
# Tentativas
# sha256 > base64 :          KHN0ZGluKT0gMjJkYmU2YjdiNzBhNjQ5NjZlMzE4MTNlNTk3ZGIzZTg2MzQ5MmQzNDFiZWUyZmIwNWMwZTg4NjQ3NzMzODdhZgo=
# sha254 > rmd160 > base64:  KHN0ZGluKT0gNDkzYmZlNDY1MjQ5NWIwZmY5MTE5YzFlM2RmMDM2MWY2YjY5NjMxOAo=
# sha1 > base64
# md5 > base64               OGM4ODVmYWEzN2Y4MWE0YjI1ZGY1ZGU0Yzc2MGI0ZjkK (mesmo tamanho)