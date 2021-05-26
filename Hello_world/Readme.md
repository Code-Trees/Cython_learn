
Running Instruction 


jd@jd:~/Desktop/Gitwork/Cython/Hello_world$ ls -ltr
total 12
-rwxrwxr-x 1 jd jd  81 May 26 22:00 hello_world.pyx
-rwxrwxr-x 1 jd jd 188 May 26 22:05 setup.py

jd@jd:~/Desktop/Gitwork/Cython/Hello_world$ python setup.py build_ext --inplace
Compiling hello_world.pyx because it changed.
[1/1] Cythonizing hello_world.pyx
/home/jd/.local/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /home/jd/Desktop/Gitwork/Cython/Hello_world/hello_world.pyx
  tree = Parsing.p_module(s, pxd, full_module_name)
/home/jd/anaconda3/envs/eva5/lib/python3.8/distutils/dist.py:274: UserWarning: Unknown distribution option: 'ext_models'
  warnings.warn(msg)
running build_ext


jd@jd:~/Desktop/Gitwork/Cython/Hello_world$ ls -ltr
total 132
-rwxrwxr-x 1 jd jd    117 May 26 22:07 setup.py
-rwxrwxr-x 1 jd jd     81 May 26 22:07 hello_world.pyx
-rw-rw-r-- 1 jd jd 122838 May 26 22:07 hello_world.c


jd@jd:~/Desktop/Gitwork/Cython/Hello_world$ python3
Python 3.8.10 (default, May 19 2021, 18:05:58) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello_world
Hello World Folks
