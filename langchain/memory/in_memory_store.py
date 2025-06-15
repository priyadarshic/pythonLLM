from langchain_core.stores import InMemoryByteStore

store = InMemoryByteStore()
store.mset([('key1', b'value1'), ('key2', b'value2')])
store.mget(['key1', 'key2'])
# [b'value1', b'value2']
store.mdelete(['key1'])
list(store.yield_keys())
# ['key2']
list(store.yield_keys(prefix='k'))
# ['key2']
