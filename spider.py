import resolver
import downloader
import task_manner
from string import split

task = task_manner.Task_manner('http://www.estedu.com')
task_lis = task.task_lis
for des in task_lis:
    try:
        content = downloader.DownLoader(des)
    except:
        task_lis.remove(des)
    content_data = resolver.Resolver(content.url_content)
    for i in content_data.srcs:
        try:
            img_data = downloader.DownLoader(i).url_content.read()
            f = open(split(i,r'/')[-1], 'wb')
        except:
            pass
        f.write(img_data)
    for i in content_data.links:
        if i not in task_lis and isinstance(i, basestring) and 'estedu' in i:
            task_lis.append(i)
            print task_lis
print len(task_lis)