# class NotImplementedError(Exception):
#     def __init__(self, m):
#         self.message = m
#     def __str__(self):
#         return self.message

class ActiveModel:
    def __init__(self):
        raise NotImplementedError("Implement this method in the child class")

    @classmethod
    def filename(cls):
        # Override this method in child class
        # This logic will only add "s" to the model name
        return f"db/{cls.__name__.lower()}s.txt"

    @classmethod
    def all(cls):
        file = open(cls.filename())
        file.seek(0)
        lines = file.readlines()
        file.close()
        collection = []
        for line in lines:
            attrs = line.strip().split(',')
            collection.append(cls(*attrs[1:],attrs[0]))
        return collection


    def save(self):
        if self.record_id:
            # Update
            with open(self.filename(), 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if line.startswith(f"{self.record_id},"):
                        file.write(self.attributes())
                    else:
                        file.write(line)
                file.truncate()
        else:
            # Add new record
            file = open(self.filename(), 'r+')
            file.seek(0)
            lines = file.readlines()
            lastline = lines and lines[-1]
            if lastline:
                pk = int(lastline.split(',')[0]) + 1
            else:
                pk = 1
            self.record_id = pk
            file.write(self.attributes())
            file.close()
        return self


    def attributes(self):
        attrs =  self.__dict__.copy()
        record_id = attrs['record_id']
        del attrs['record_id']
        attrs_list = [str(i) for i in attrs.values()]
        return(f"{record_id},{','.join(attrs_list)}\n")

    @classmethod
    def delete(cls, record_id):
        with open(cls.filename(), 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not line.startswith(f"{record_id},"):
                    file.write(line)
            file.truncate()

    @classmethod
    def find(cls, record_id):
        with open(cls.filename()) as file:
            for line in file:
                if line.startswith(f"{record_id},"):
                    instance = cls(*line.strip().split(',')[1:],record_id)

                    return instance

    @classmethod
    def find_with_alert(cls, record_id):
        record = cls.find(record_id)
        if not record:
            print("Record not found")
            return
        return record

