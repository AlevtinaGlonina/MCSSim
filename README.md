The following Debian packages are required:

python-cheetah, cmake, make, g++ 

Build:

cd MCSSim
cmake CMakeLists.txt
cd generator
./build.sh

Run parametrized model:

./model_builder test.xml > out.xml
