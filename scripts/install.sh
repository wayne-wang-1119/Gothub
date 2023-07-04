set -e

python -m pip install \
    -e "./gots[dev,test]" \
    -e "./gothub[dev,test]"
