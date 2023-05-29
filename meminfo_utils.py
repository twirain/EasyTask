import re


def parse_app_summary(meminfo: str):
    ret = {}
    reach = False
    for line in meminfo.splitlines():
        if not reach and 'App Summary' in line:
            reach = True
            continue
        if not reach:
            continue

        _pick_field('Java Heap', line, ret)
        _pick_field('Native Heap', line, ret)
        _pick_field('Code', line, ret)
        _pick_field('Stack', line, ret)
        _pick_field('Graphics', line, ret)
        _pick_field('Private Other', line, ret)
        _pick_field('System', line, ret)
        _pick_field('TOTAL', line, ret)

        if ret.get('TOTAL') is not None:
            break
    return ret


def parse_objects(meminfo: str):
    ret = {}
    reach = False
    for line in meminfo.splitlines():
        if not reach and 'Objects' in line:
            reach = True
            continue
        if not reach:
            continue

        _pick_field('Views', line, ret)
        _pick_field('ViewRootImpl', line, ret)
        _pick_field('AppContexts', line, ret)
        _pick_field('Activities', line, ret)
        _pick_field('Assets', line, ret)
        _pick_field('AssetManagers', line, ret)
        _pick_field('Local Binders', line, ret)
        _pick_field('Proxy Binders', line, ret)
        _pick_field('Parcel memory', line, ret)
        _pick_field('Parcel count', line, ret)
        _pick_field('Death Recipients', line, ret)
        _pick_field('OpenSSL Sockets', line, ret)
        _pick_field('WebViews', line, ret)

        if ret.get('WebViews') is not None:
            break
    return ret


def _pick_field(name, str_line, dict_ret):
    if dict_ret.get(name) is not None:
        return
    ret = re.findall(fr"{name}:\s+(\d+)", str_line)
    if len(ret) != 0:
        dict_ret[name] = int(ret[0])


if __name__ == '__main__':
    txt = """
   Applications Memory Usage (in Kilobytes):
Uptime: 2506973082 Realtime: 2518463375

** MEMINFO in pid 23844 [com.cf.awevfx] **
                   Pss  Private  Private  SwapPss     Heap     Heap     Heap
                 Total    Dirty    Clean    Dirty     Size    Alloc     Free
                ------   ------   ------   ------   ------   ------   ------
  Native Heap   383073   382944        0       62   436736   404535    32200
  Dalvik Heap    12734    12684        0       21    23770    11885    11885
 Dalvik Other     5292     5292        0        3                           
        Stack      112      112        0        0                           
       Ashmem      182      168        0        0                           
    Other dev      272      232       20        0                           
     .so mmap    11613     1012     4140       53                           
    .jar mmap     7724        0     4324        0                           
    .apk mmap    15588      272    13272        0                           
    .ttf mmap     1335        0     1032        0                           
    .dex mmap    34202    32184     1972      168                           
    .oat mmap      205        0       16        0                           
    .art mmap    10075     9260       88       46                           
   Other mmap    11000      704     8832        0                           
    GL mtrack   207372   207372        0        0                           
      Unknown     5186     5120        0       10                           
        TOTAL   706328   657356    33696      363   460506   416420    44085
 
 App Summary
                       Pss(KB)
                        ------
           Java Heap:    22032
         Native Heap:   382944
                Code:    58224
               Stack:      112
            Graphics:   207372
       Private Other:    20368
              System:    15276
 
               TOTAL:   706328       TOTAL SWAP PSS:      363
 
 Objects
               Views:      305         ViewRootImpl:        1
         AppContexts:        9           Activities:        3
              Assets:        9        AssetManagers:        0
       Local Binders:       55        Proxy Binders:       46
       Parcel memory:       24         Parcel count:      103
    Death Recipients:        1      OpenSSL Sockets:       14
            WebViews:        0
 
 SQL
         MEMORY_USED:      934
  PAGECACHE_OVERFLOW:      281          MALLOC_SIZE:      117
 
 DATABASES
      pgsz     dbsz   Lookaside(b)          cache  Dbname
         4       96            109      11/108/13  /data/user/0/com.cf.awevfx/no_backup/androidx.work.workdb
         4        8                         0/0/0    (attached) temp
         4       96             33         2/32/3  /data/user/0/com.cf.awevfx/no_backup/androidx.work.workdb (3)
         4       24             83       99/54/10  /data/user/0/com.cf.awevfx/databases/thinkingdata
         4       52            108       17/68/14  /data/user/0/com.cf.awevfx/databases/bugly_db_

   """
    print(f"app_summary={parse_app_summary(txt)}")
    print(f"objects={parse_objects(txt)}")
