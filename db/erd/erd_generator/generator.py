from db.table_info import *
from db.erd.erd_generator.constants import *
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from eralchemy2 import render_er


def class_factory(name, argDict, BaseClass):
    def __init__(self, argDict):
        for key in argDict:
            setattr(self, key, argDict[key])

    argDict["__init__"] = __init__
    newclass = type(name, (BaseClass,), argDict)
    return newclass


def erd_generator(db_name, db_pk_info, tables):
    Base = declarative_base()
    for table in tables:
        para_dict = {
            "__tablename__": table
        }
        if table in db_pk_info:
            for field in tables[table]:
                para_dict[field] = Column(TYPE_MAP[tables[table][field]],
                                          primary_key=db_pk_info[table] == field)
        else:
            para_dict["id"] = Column(Integer, primary_key=True)
            for field in tables[table]:
                pk_table = None
                if field in db_pk_info.values():
                    for key, value in db_pk_info.items():
                        if value == field:
                            pk_table = key
                            break
                if pk_table:
                    para_dict[field] = Column(ForeignKey(f'{pk_table}.{field}'))
                else:
                    para_dict[field] = Column(TYPE_MAP[tables[table][field]])
        temp_class = class_factory(
            name=table,
            argDict=para_dict,
            BaseClass=Base
        )
    file_name = db_name.split("_")[1]
    render_er(Base, output=f"../db/{file_name}/{file_name}.png")
    render_er(Base, output=f"../db/{file_name}/{file_name}.pdf")


def create_table_dict(db):
    rows = get_db_tables(db)
    tables = [row[0] for row in rows]
    table_info = dict()
    for table in tables:
        rows = get_columns_and_type(db, table)
        table_info[table] = {}
        for row in rows:
            table_info[table][row[0]] = row[1]
    return table_info


if __name__ == "__main__":
    print("PRECENT COMPLETE", end='')
    count = 0
    total = len(DB_NAMES)
    for db in DB_NAMES:
        if not count: print(" => START", end="")
        table_info = create_table_dict(db)
        erd_generator(db, DB_NAMES[db]["pk"], table_info)
        count += 1
        print(f" => {100*count/total}%", end='')
