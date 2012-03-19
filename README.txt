

With this package you can add a part like the following to your buildout.

This will install a script bit/my_android_sdk, which can be used for installing the android sdk, like so:

./bin/my_android_ndk install

[my_android_ndk]
recipe = bit.recipe.android_ndk
version = r7
ndk = http://dl.google.com/android/ndk/android-ndk-r7-linux-x86.tar.bz2
