# News AI mobile app

This is the Flutter client project. From this directory, install dependencies
and run it on a connected device or simulator:

```bash
flutter pub get
flutter run
```

See the repository [README](../../README.md) for backend startup and
device-specific API URL configuration. The current UI is still the Flutter
counter demo; the API URL constant is not yet used by a client.

Application code is organized by responsibility: `lib/main.dart` starts the
app, `lib/core/config/` contains shared configuration, and
`lib/features/` contains feature-specific UI and behavior.
