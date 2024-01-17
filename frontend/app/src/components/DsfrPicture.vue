<script setup lang="ts">
import { DsfrPicture } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		// Props
		size?: 'small' | 'medium' | 'large'
		src?: string
		alt?: string
		title?: string
		legend?: string
		ratio?: '32x9' | '16x9' | '3x2' | '4x3' | '1x1' | '3x4' | '2x3'
	}>
>()
</script>

<template>
	<div class="component">
		<DsfrPicture
			v-bind="props.args"
		>
		</DsfrPicture>
	</div>
</template>

<style scoped>
.component :deep(.fr-content-media) {
	margin-top: 0;
	margin-bottom: 0;
}
</style>
