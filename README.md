# jdk-jce RPM

Oracle JDK's JCE dependencies

This RPM adds the necessary JCE JARs to permit unlimited strength cryptography. These JARs are major version specific (i.e. Java 8).
They're used by the JDK version specific jdk-helper RPM to overwrite the default JCE JARs which only permit low strength cryptography.

You *must* accept the Oracle Binary License (linked in the .spec file with text copy in this repo) in order to use these JARs.

The license for the code creating the RPM is Apache 2.0 Public License.

## Making the RPM
The RPM only requires:
* make
* rpmbuild
* the major version number of the Oracle JDK RPM to create a jdk-devel rpm for
* the JCE JARs (URL in spec file, requires agreement of the Oracle binary license in LICENSE.txt)

Syntax:
```
make JDK_MAJOR=8
```

The leading '1' in JDK 1.8 is assumed at this time.
