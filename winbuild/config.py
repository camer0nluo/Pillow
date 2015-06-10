SF_MIRROR = 'http://hivelocity.dl.sourceforge.net'
SF_MIRROR = 'http://iweb.dl.sourceforge.net'

pythons = {#'26':7, 
           '27':7, 
           #'32':7, 
           '33':7.1, 
           '34':7.1}

VIRT_BASE = "c:/vp/"

libs = { 'zlib':{
    'url':'http://zlib.net/zlib128.zip',
    'hash': 'md5:126f8676442ffbd97884eb4d6f32afb4',
    'dir': 'zlib-1.2.8',
    },
         'jpeg':{
    'url':'http://www.ijg.org/files/jpegsr9a.zip',
    'hash': 'md5:a34f3c82760270ee1e1885b15b90a72e', # not found - generated by wiredfool
    'dir': 'jpeg-9a',
    },
         'tiff':{
    'url':'ftp://ftp.remotesensing.org/pub/libtiff/tiff-4.0.3.zip',
    'hash': 'md5:dd70349cedb3981371686e1c9b89a7f9', # not found - generated by wiredfool
    'dir': 'tiff-4.0.3',
   },
         'freetype':{
    'url':'http://download.savannah.gnu.org/releases/freetype/ft253.zip',
    'hash': 'md5:b3858f7e69740ac04ef53366aeb172bc', # not found - generated by wiredfool
    'dir': 'freetype-2.5.3',
    },
         'lcms':{
    'url':SF_MIRROR+'/project/lcms/lcms/2.6/lcms2-2.6.zip',
    'hash': 'sha1:eea25f001246fa2e6b242ac456cecff7483cf061',
    'dir': 'lcms2-2.6',
   },
         'tcl':{
    'url':SF_MIRROR+'/project/tcl/Tcl/8.5.13/tcl8513-src.zip',
    'hash': 'sha1:3e01585c91293c532a3cd594ec59deca92153a5e',
    'dir': '',
   },
         'tk':{
    'url':SF_MIRROR+'/project/tcl/Tcl/8.5.13/tk8513-src.zip',
    'hash': 'sha1:23a1d7ddd416e11e06dfdb9f86111d4bab9420b4',
    'dir': '',
    },
         'webp':{
    'url':'https://webp.googlecode.com/files/libwebp-0.4.0.tar.gz',
    'hash':'sha1:326c4b6787a01e5e32a9b30bae76442d18d2d1b6',
    'dir':'libwebp-0.4.0',
    },
#         'openjpeg':{
#    'url':'https://openjpeg.googlecode.com/files/openjpeg-2.0.0.tar.gz',
#    'hash':'sha1:0af78ab2283b43421458f80373422d8029a9f7a7',
#    'dir':'openjpeg-2.0.0',
#    },

         'openjpeg':{
    'url':SF_MIRROR+'/project/openjpeg/openjpeg/2.1.0/openjpeg-2.1.0.tar.gz',
    'hash':'md5:f6419fcc233df84f9a81eb36633c6db6',
    'dir':'openjpeg-2.1.0',
    },

     }

bin_libs = {
         'openjpeg':{
             'filename':'openjpeg-2.0.0-win32-x86.zip',
             'hash':'sha1:xxx',
             'version':'2.0'
    },
         }

compilers = { (7,64): {
    'env_version':'v7.0',
    'vc_version':'2008',
    'env_flags': '/x64 /xp',
    'inc_dir': 'msvcr90-x64',
    'platform': 'x64'
    },
             (7,32): {
    'env_version':'v7.0',
    'vc_version':'2008',
    'env_flags': '/x86 /xp',
    'inc_dir': 'msvcr90-x32',
    'platform': 'Win32'
   },

             (7.1,64): {
    'env_version':'v7.1',
    'vc_version':'2010',
    'env_flags': '/x64 /vista',
    'inc_dir': 'msvcr10-x64',
    'platform': 'x64',
   },
             (7.1,32): {
    'env_version':'v7.1',
    'vc_version':'2010',
    'env_flags': '/x86 /vista',
    'inc_dir': 'msvcr10-x32',
    'platform': 'Win32',
    },

    }
