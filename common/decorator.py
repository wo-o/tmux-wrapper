def method_decorator(func):
    def wrapper(self,args=''):
        print('\n'*1+'_'*100+'\n'*2)
        if not args:
            res_code = func(self)
        else:
            res_code = func(self, args)
        print('\n'*1+'_'*100+'\n'*1)
        return res_code
    return wrapper

def function_decorator(func):
    def wrapper(args=''):
        print('\n'*1+'_'*100+'\n'*2)
        if not args:
            res_code = func()
        else:
            res_code = func(args)
        print('\n'*1+'_'*100+'\n'*1)
        return res_code
    return wrapper
