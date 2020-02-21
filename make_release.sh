export COPY_EXTENDED_ATTRIBUTES_DISABLE=true

mkdir temp
mkdir temp/dreammaker_fx_1.5.3

cp -R ~/Documents/Arduino/hardware/dreammaker_fx/samd/* temp/dreammaker_fx_1.5.3/

mkdir temp/dreammaker_fx_1.5.3/libraries/dmfx
cp -R ~/Documents/Arduino/libraries/dmfx-arduino/* temp/dreammaker_fx_1.5.3/libraries/dmfx/

#mkdir temp/dreammaker_fx_1.1.0/examples
#mkdir temp/dreammaker_fx_1.1.0/examples/dmfx_firmware_updater
#cp -R ~/Github/Dreammaker_FX/dmfx-firmware-updater/dmfx-firmware-updater/* temp/dreammaker_fx_1.1.0/examples/dmfx_firmware_updater/

mkdir temp/dreammaker_fx_1.5.3/bootloaders

rm arduino-board-index/boards/dreammaker_fx-samd-1.5.3.tar.bz2
cd temp/
tar --exclude=".DS_Store" --disable-copyfile -cvjSf ../arduino-board-index/boards/dreammaker_fx-samd-1.5.3.tar.bz2 *
#tar -czvf ../../arduino-board-index/boards/dreammaker_fx-samd-1.1.0.tar.gz  *
cd ..
echo "SHA256:"
shasum -a 256 arduino-board-index/boards/dreammaker_fx-samd-1.5.3.tar.bz2

echo "SIZE:"
stat -x arduino-board-index/boards/dreammaker_fx-samd-1.5.3.tar.bz2

rm -R temp