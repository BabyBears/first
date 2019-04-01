#快速排序
def quick(value):
    #递归的退出条件
    if len(value) < 2:
        return value
    #设置关键数据
    mark = value[0]
    #找出所有比关键数据小的
    small = [x for x in value if x < mark]
    #找出所有比关键数据大的
    big = [x for x in value if x > mark]
    #找出所有比关键数据相等的
    equal = [x for x in value if x == mark]
    return quick(small) + equal + quick(big)

        

if __name__ == "__main__":

    value = [100,120,80,60,78,66,68,98,99,102]
    quick(value)
    value = quick(value)
    print("排序后：",value)