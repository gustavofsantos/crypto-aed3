hash="AKCkKOEHZuUPfCLbS0ye8WFnXoDEgw9RFYXlw293vbY="
status="not found"

while read -r LINE; do
  output=`echo -n $LINE | openssl dgst -sha256 -binary | openssl base64`
  if [ $output == $hash ]
  then
    echo "Found! $LINE"
    status="found"
    break
  fi
done  < $1 > output

echo status