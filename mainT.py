from config.seetings import unid_list
from storage.db import init_db
from storage.storage_base_parent_unid_info import save_all_unid

def main():
    init_db()

    save_all_unid()


if __name__ == '__main__':
    main()

