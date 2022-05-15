from gendiff import generate_diff


def test_gendiff():
    path1 = "tests/fixtures/file1_plane.json"
    path2 = "tests/fixtures/file2_plane.json"
    with open("tests/fixtures/plane_difference.txt") as text:
        expecting = text.read()
    result = generate_diff(path1, path2)
    assert result == expecting
