from task_2 import logger


@logger('generator.log')
def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item


flat_generator([1, [2, 3, 4], [['a']]])
