# first line: 97
            @memory.cache
            def make_rname(*args):
                # uuid should be unique, but check just in case
                while True:
                    fname = str(uuid.uuid4()).replace('-', '')
                    if not os.path.isdir(os.path.join(self.cachedir, fname)):
                        break
                return fname
