<script setup lang="ts">
import { reactive } from 'vue'
import { DsfrAlert } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		title?: string
		description?: string
		type?: 'error' | 'success' | 'warning' | 'info'
		small?: boolean
		closed?: boolean
		closeable?: boolean
		titleTag?: 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6'
		id?: string
	}>
>()
</script>

<template>
	<div class="component">
		<DsfrAlert v-bind="props.args" />
	</div>
</template>
