immutable_tuple = (123, True, 7.8, 'Grenade')
print(immutable_tuple)
immutable_tuple = [0][0] = False # изменяет все элементы кортежа
print(immutable_tuple)
mutable_list = ['Bullet', 'Rocket', 'Grenade']
mutable_list[1] = 'Missile'
print(mutable_list)
mutable_list.append('Rocket')
print(mutable_list)
mutable_list.append(89.5)
print(mutable_list)
