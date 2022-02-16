import scrapinghub


class CollectionHelper:
    """Adapter to make interacting with scraping collection easier"""
    def __init__(self, proj_id, collection_name, api_key=None, create=False):
        sh_client = scrapinghub.ScrapinghubClient(api_key)
        project = sh_client.get_project(proj_id)
        collections = project.collections
        self.store = collections.get_store(collection_name)
        self.writer = self.store.create_writer()
        if create:
            # a store is created by writing into it
            # if create is true, write and then delete a placeholder
            self.store.set({'_key': 'placeholder', 'value': 123})
            self.delete(['placeholder'])

    def get(self, key, default=None):
        """
        Gets value of key
        Args:
            key: Key searching for
            default: What to return if key not present
        Returns:
            The value of item with the key in collection or the default if not present.
        """
        # I use the .list method here because .get only returns bytes.
        search = self.store.list([key])
        if not search:
            return default
        return search[0]['value']

    def set(self, key, value, flush=False):
        """
        Set value at key
        Args:
            key: The key for the item
            value: Thew value for the item
            flush(bool): Whether to flush the writer
        """
        self.writer.write({'_key': key, 'value': value})
        if flush:
            # This is using a batch writer and will not write if the batch isn't filled
            # The flush option will flush the writer, causing anything in the current batch to be written
            self.flush_writer()

    def delete(self, keys):
        """
        Delete keys from store.
        Args:
            keys(list): List of keys to delete
        """
        self.store.delete(keys)

    def flush_writer(self):
        """
        Flush the writer
        """
        self.writer.flush()

    def iter_items(self):
        """
        Create an iterable over all items in the collection
        Returns(generator)
        """
        return self.store.iter()

    def list_items(self):
        """
        Create a list of all items in the collection
        Returns(list)
        """
        return list(self.iter_items())

    def list_keys(self):
        """
        Get a list of all keys in the collection
        Returns(list)
        """
        items_generator = self.iter_items()
        keys = [i['_key'] for i in items_generator]
        return keys

    def list_values(self):
        """
        Get a list of all keys in the collection
        Returns(list)
        """
        items_generator = self.iter_items()
        values = [i['value'] for i in items_generator]
        return values