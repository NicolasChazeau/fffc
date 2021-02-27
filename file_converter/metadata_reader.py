class MetadataReader:
    @staticmethod
    def parse_metadata(metadata_iterator):
        col_list = []
        for line in metadata_iterator:
            col_name, col_size, col_type = line.split(",")
            col_list.append({
                "name": col_name,
                "size": col_size,
                "type": col_type
            })
        return col_list
