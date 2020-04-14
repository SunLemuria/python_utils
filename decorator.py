# 带定长参数的装饰器
def new_func(func):
    def wrappedfun(username, pd):
        if username == 'root' and pd == '123':
            print('verified')
            return func()
        else:
            print('error verifying')
            return

    return wrappedfun


@new_func
def origin():
    print('executing')


origin('root', '123')


# 带不定长参数的装饰器
def new_func(func):
    def wrappedfun(*parts):
        if parts:
            counts = len(parts)
            print('本系统包含:', end='')
            for part in parts:
                print(part, end='')
            print('等', counts, '部分')
            return func()
        else:
            print('用户名或密码错误')
            return func()

    return wrappedfun


@new_func
def origin():
    print('开始执行函数')


origin('硬件', '软件', '用户数据')


# 同时带不定长, 关键字参数的装饰器
def new_func(func):
    def wrappedfun(*args, **kwargs):
        if args:
            counts = len(args)
            print('本系统包含 ', end='')
            for arg in args:
                print(arg, ' ', end='')
            print('等', counts, '部分')
            if kwargs:
                for k in kwargs:
                    v = kwargs[k]
                    print(k, '为:', v)
            return func()
        else:
            if kwargs:
                for kwarg in kwargs:
                    print(kwarg)
                    k, v = kwarg
                    print(k, '为:', v)
        return func()

    return wrappedfun


@new_func
def origin():
    print('开始执行函数')


origin('硬件', '软件', '用户数据', 总用户数=5, 系统版本='CentOS 7.4')
