from decorator import decorator


@decorator
def replace_with_models(f, *args, **kwargs):
    for var, val in kwargs.iteritems():
        try:
            model_name = var[0].upper() + var[1:]
            module = __import__('launcher.apps.rocket.models', globals(),
                locals(), [model_name], -1)
            model = getattr(module, model_name)
            try:
                kwargs[var] = model.objects.get(pk=val)
            except model.DoesNotExist:
                kwargs[var] = False
        except (ImportError, AttributeError):
            pass

    return f(*args, **kwargs)
