def Settings(**kwargs):
    return{
            'flags':['-x','c++','-Wall','-Wextra','-Werror',
                '-I','/usr/include/',
                '-I','../include/',
                '-I','./',
                '-I','../../../ngx_cpp_dev/ngxpp/',
                '-I','../../../ngx_cpp_dev/ngxpp/config/',
                '-I','/home/svandex/nginx_src/src/http/',
                '-I','/home/svandex/nginx_src/src/core/',
                '-I','/home/svandex/nginx_src/src/objs',
                '-I','/home/svandex/nginx_src/src/event',
                '-I','/home/svandex/nginx_src/src/stream',
                '-I','/home/svandex/nginx_src/src/mail',
                '-I','/home/svandex/nginx_src/src/modules',
                '-I','/home/svandex/nginx_src/src/os/unix',
                '-I','/home/svandex/nginx_src/src/misc/',
                '-I','../sqlitecpp/include',
                ]
            }