from django.conf import settings
from django.core.management.base import CommandError
from optparse import make_option
import re
import sys


try:
    from south.management.commands.test import Command as BaseCommand
except ImportError:
    from django.core.management.commands.test import Command as BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-r', '--coverage-report',
            action='store',
            dest='coverage_report',
            help='Which coverage report to use (html or xml).'),
        make_option('-d', '--coverage-report-dir',
            action='store',
            dest='coverage_report_dir',
            help='Path to write coverage reports to.'),
        make_option('-o', '--coverage-omit',
            action='store',
            dest='coverage_omit',
            help='Partial paths to omit from coverage.'),
    )

    ignore = [
        '^django\.contrib',
        '^south$',
        '^django_',
    ]

    omit = [
        '*tests*',
        '*migrations*',
        '*management*',
        '*urls*',
        '*site-packages*',
    ]

    exclude_lines = [
        'def __unicode__',
        'def __repr__',
        'if settings.DEBUG',
        'raise NotImplementedError',
        'from django\.',
    ]

    def handle(self, *args, **options):
        try:
            import coverage
        except ImportError:
            raise CommandError('Please install coverage. http://j.mp/moEM7y')

        apps = settings.INSTALLED_APPS
        omit = Command.omit

        coverage_omit = options.get('coverage_omit')
        if coverage_omit:
            omit += ['*%s*' % o for o in coverage_omit.split(',')]

        report_dir = options.get('coverage_report_dir')
        report_type = options.get('coverage_report')
        if report_type and report_type.lower() not in ['xml', 'html']:
            raise CommandError("'%s' is not a valid report option." %
                report_type)

        if report_type and not report_dir:
            raise CommandError("Please specifiy an output directory " + \
                "for the %s coverage reports." % report_type.upper())

        include = []
        for a in apps:
            partial_path = a.replace('.', '/')
            include_app = True
            for i in Command.ignore:
                if re.search(i, a):
                    include_app = False
                    break

            if include_app:
                include.append('*%s*' % partial_path)
                omit.append('*%s/admin*' % partial_path)

        reporter = coverage.coverage(include=include, omit=omit,
            config_file=False)

        for l in Command.exclude_lines:
            reporter.exclude(l)

        reporter.start()
        BaseCommand.handle(self, *args, **options)
        reporter.stop()

        print "--------------------------------------------------------------"
        print "Included: %s" % ', '.join(include)
        print "Omitting: %s" % ', '.join(omit)
        print "Excluding Lines: %s" % ', '.join(reporter.config.exclude_list)
        print "--------------------------------------------------------------"

        reporter.report(include=include, omit=omit, file=sys.stdout)

        if not report_type:
            return
        else:
            report_type = report_type.lower()

        writer = getattr(reporter, '%s_report' % report_type.lower())
        dest = report_dir
        if report_type == 'html':
            writer(directory=report_dir)
        else:
            dest += '/coverage.xml'
            writer(outfile='%s/coverage.xml' % report_dir)

        print "--------------------------------------------------------------"
        print "Wrote %s report to %s." % (report_type.upper(), dest)
