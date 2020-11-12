#自定义包的打包与发布

1. 文件目录结构

        .
        ├── my_package
        │   └── __init__.py
        └── setup.py

2. setup.py 中的内容
    ```python
    from setuptools import setup, find_packages
    
    setup(
            name='my_package',     # 包名字
            version='1.0',   # 包版本
            description='',   # 简单描述
            author='dosea',  # 作者
            author_email='doosea@163.com',  # 作者邮箱
            url='https://github.com/doosea/mypackage.git',      # 包的主页
            packages=find_packages()                # 包
    )  

    ```

3. __init__.py 
    ```python
    def china():
        print("China NO.1")
    
    
    def my_package():
       print("this is my_package!")
    
    
    if __name__ == '__main__':
        my_package()
        china()
    ```

4. 制作 wheel 文件

    `python setup.py bdist_wheel`

5. 打包编译后的文件目录结构

        .
        ├── build
        │   ├── bdist.linux-x86_64
        │   └── lib
        │       └── my_package
        │           └── __init__.py
        ├── dist
        │   └── my_package-1.0-py3-none-any.whl
        ├── my_package
        │   └── __init__.py
        ├── my_package.egg-info
        │   ├── dependency_links.txt
        │   ├── PKG-INFO
        │   ├── SOURCES.txt
        │   └── top_level.txt
        └── setup.py
        
6. 使用.whl 文件安装依赖库
    
    `pip install my_package-1.0-py3-none-any.whl`
    
7. 使用自定义的包
    
   ```python
    import my_package
    my_package.china()
    my_package.my_package()
   ```