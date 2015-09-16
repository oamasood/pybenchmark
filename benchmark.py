__author__ = 'oamasood'

"""
For now, does: if list_obj vs if len(list_obj) vs if custom_obj vs if len(custom_obj).

"""

import time
import numpy

NUM_REPS = 2 ** 19
NUM_SETS = 2 * 12


class CoolObject:
    def __init__(self, cool_list):
        self.list_obj = cool_list

    def __len__(self):
        return len(self.list_obj)

    def __eq__(self, other):
        return isinstance(other, CoolObject) and other.list_obj == self.list_obj


def benchmark_if_vs_if_len():
    print "Testing out if <list> vs if len(<list>) vs if <obj> vs if len(<obj>)"

    set_results = {'if <list>': [], 'if len(<list>)': [], 'if <obj>': [], 'if len(<obj>)': []}

    def do_rep_and_add_to_results(set_results, method_name, obj_to_check, is_check_with_len):
        rep_index = 0
        start_reps_time = time.clock()
        if is_check_with_len:
            while rep_index < NUM_REPS:
                if len(obj_to_check):
                    rep_index += 1  # So interpreter doesn't optimize it
        else:
            while rep_index < NUM_REPS:
                if obj_to_check:
                    rep_index += 1  # So interpreter doesn't optimize it
        end_time = time.clock()
        if not set_results.get(method_name):
            set_results[method_name] = []
        set_results[method_name].append(end_time - start_reps_time)
        print "End time for %s set #%s: %s" % (method_name, set_index, set_results[method_name][-1])

    set_index = 0
    while set_index < NUM_SETS:
        list_obj = CoolObject([1, 2, 3])

        do_rep_and_add_to_results(set_results, 'if <obj>', list_obj, False)

        do_rep_and_add_to_results(set_results, 'if len(<obj>)', list_obj, True)

        list_obj = [1, 2, 3]
        do_rep_and_add_to_results(set_results, 'if <list>', list_obj, False)

        do_rep_and_add_to_results(set_results, 'if len(<list>)', list_obj, True)

        set_index += 1
        # time.sleep(0.25)

    print "Results: %s" % set_results
    for method_name, results in set_results.items():
        print "Method %s avg: %s, stddev: %s%%" % (
            method_name, numpy.mean(results), 100.0 * numpy.std(results) / numpy.mean(results))


benchmark_if_vs_if_len()
