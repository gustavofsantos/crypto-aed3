# gen data
python gen_data_chave2.py

# change dir
mkdir combs && cd combs

# split file
split -l 200000 --numeric-suffixes ../combinations.txt comb

# import all to IPFS