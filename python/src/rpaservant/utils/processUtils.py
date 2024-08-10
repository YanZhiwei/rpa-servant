import psutil

class ProcessUtil(object):
    @staticmethod
    def kill(process_name: str) -> bool:
        if process_name is None or process_name == "":
            return False
        for proc in psutil.process_iter():
            try:
                pname = proc.name()
                if process_name.lower() == pname.lower():
                    proc.kill()
                return True
            except Exception as e:
                return False
