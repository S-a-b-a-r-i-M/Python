from Linked_List import MyLinkedList


def main():
    linked_list = MyLinkedList()
    linked_list.insert_at_beginning(40)
    linked_list.insert_at_beginning(30)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(10)

    linked_list.insert_at_end(50)
    linked_list.insert_at_end(60)

    linked_list.insert_values([70, 80, 90, 100])

    print(linked_list.insert(0, 0))
    print(linked_list.insert(11, 110))

    linked_list.show()

    print('Length :', linked_list.length)  # CALLS THE GETTER METHOD

    print('removing 1st index:', linked_list.remove_at(1))
    print('removing 0 index:', linked_list.remove_at(0))
    print('removing last index:', linked_list.remove_at(linked_list.length))
    linked_list.show()
    print('obj :',linked_list)


if __name__ == '__main__':
    main()
