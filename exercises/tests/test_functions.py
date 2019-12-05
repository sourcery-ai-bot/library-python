# pylint: disable=redefined-outer-name
import pytest
from exercises.find_matching_pairs import find_matching_pairs


class TestFindMatchingPairs:
    @pytest.mark.parametrize('original_list, target_num, result',
                            [
                                ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [(1, 2)]),
                                ([1, 2, 3, 4, 5, 6], 9, [(3, 6), (4, 5)]),
                                ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12, [(1, 11),
                                    (2, 10), (3, 9), (4, 8), (5, 7)]),
                                ([1, 2], 12, []),
                                ([-1, -2], 12, []),
                            ]
                            )
    def test_find_matching_pairs(self, original_list, target_num, result):
        assert find_matching_pairs(original_list, target_num) == result
