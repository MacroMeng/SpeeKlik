import logging
import os


log = logging.getLogger()
output_fn = ""


def init_logger():
    global output_fn, log
    os.makedirs("../logs/", exist_ok=True)
    log_files = [fn for fn in os.listdir("../logs/") if fn.endswith(".log") and fn.startswith("LOG")]
    if len(log_files) >= 5:
        os.remove("../logs/LOG1.log")
        for i, org_fn in enumerate(log_files[1:]):
            new_fn = f"LOG{i+1}.log"
            os.rename(f"../logs/{org_fn}", f"../logs/{new_fn}")
        output_fn = "../logs/LOG5.log"
    else:
        output_fn = f"../logs/LOG{len(log_files)+1}.log"

    log.setLevel(logging.DEBUG)
    logging.basicConfig(filename=output_fn,
                        style='{',
                        format="[{asctime}|{levelname}|{module}] {message}",
                        encoding="utf-8")
