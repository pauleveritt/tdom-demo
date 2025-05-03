try:
    import playwright

    pytest_plugins = "tdom_demo.fixtures"
except ImportError:
    pass
