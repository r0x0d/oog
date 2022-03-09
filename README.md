[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/r0x0d/oogg/main.svg)](https://results.pre-commit.ci/latest/github/r0x0d/oogg/main)
[![Coverage](https://github.com/r0x0d/oogg/actions/workflows/coverage.yml/badge.svg)](https://github.com/r0x0d/oogg/actions/workflows/coverage.yml)
[![codecov](https://codecov.io/gh/r0x0d/oogg/branch/main/graph/badge.svg?token=5APPY0PPK4)](https://codecov.io/gh/r0x0d/oogg)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/r0x0d/oogg.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/r0x0d/oogg/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/r0x0d/oogg.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/r0x0d/oogg/context:python)

# OOGG

This tools aim to be a helper to open files at the GitHub or GitLab page without
going and try to search it in their UI.

I made this because I was switching throught a lot of files daily and sometimes
I wanted to see them on GitHub because of the jump to code feature.

This tool is mostly useless.

# Usage

This is a simple tool, all you have to do in order to use it is simply go to
your local repository folder and ran it. For example, let's see it in action
using this own repository.

```bash
git clone git@github.com:r0x0d/oogg.git
cd oogg
oogg LICENSE#2
Hooray! We have successfully opened your file in yourprefered browser.

# Resulting URL in your prefered browser: https://github.com/r0x0d/oogg/blob/test-pipe/LICENSE#L2
```

# Note

Windows and MacOS are not currently supported. If you would like to see this
tool in different systems, feel free to fork it and open a PR.
