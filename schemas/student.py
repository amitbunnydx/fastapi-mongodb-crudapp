#schemas helo to serialize and also convert mongodb format json to our UI needed json

def studentEntity(de_item)->dict:
    return {

        'id':str(de_item['_id']),
        'name': de_item["student_name"],
        'email': de_item["student_email"],
        'phone': de_item["student_phone"],

    }

def listOfStudentEntity(db_item_list)-> list:
    list_stud_entity=[]
    for item in db_item_list:
        list_stud_entity.append(studentEntity(item))

    return list_stud_entity